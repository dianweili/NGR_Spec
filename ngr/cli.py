from __future__ import annotations
import argparse
import logging
import sys
from ngr.config import load_features
from ngr.mapping.report import lineage_report
from ngr.parse.runner import ParseError
from ngr.paths import P
from ngr.pipeline import (EXIT_OK, EXIT_PARSE, run_pipeline, run_pipeline_enrich,
                          run_pipeline_feature_evolution, run_pipeline_meeting_digests,
                          run_pipeline_remap, run_fetch_docs)

run_remap, run_enrich = run_pipeline_remap, run_pipeline_enrich
run_meeting_digests = run_pipeline_meeting_digests

def run_doctor(**kwargs):
    from ngr.ops.doctor import run_doctor as doctor
    return doctor(**kwargs)

def build_lineage_report():
    import json
    return lineage_report(load_features(), [json.loads(p.read_text(encoding="utf-8")) for p in sorted(P.parsed.rglob("events.json"))])

def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(prog="ngr", description="6G RAN 进展跟踪")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run"); run.add_argument("--no-llm", action="store_true"); run.add_argument("--wg", action="append"); run.add_argument("--force", action="store_true")
    backfill = sub.add_parser("backfill"); backfill.add_argument("--wg", required=True); backfill.add_argument("--from", dest="frm", type=int, required=True); backfill.add_argument("--to", type=int, required=True); backfill.add_argument("--no-llm", action="store_true")
    sub.add_parser("remap"); sub.add_parser("lineage-report")
    enrich = sub.add_parser("enrich")
    enrich.add_argument("--max-calls", type=lambda value: _positive_int(value, "--max-calls"))
    enrich.add_argument("--batch-size", type=lambda value: _positive_int(value, "--batch-size"))
    meeting_digests = sub.add_parser("meeting-digests", help="仅生成会议内 6G 特性综述")
    meeting_digests.add_argument("--max-calls", type=lambda value: _positive_int(value, "--max-calls"))
    evolution = sub.add_parser("feature-evolution", help="生成并续跑特性跨会议演进")
    evolution.add_argument("--max-calls", type=lambda value: _positive_int(value, "--max-calls"))
    doctor = sub.add_parser("doctor"); doctor.add_argument("--network", action="store_true", help="额外探测 3GPP 连通性")
    docs = sub.add_parser("fetch-docs", help="按需下载指定议程项的 TDoc 正文"); docs.add_argument("--wg", required=True); docs.add_argument("--meeting", type=int, required=True); docs.add_argument("--agenda", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "run": result = run_pipeline(wgs=args.wg, use_llm=not args.no_llm, force=args.force)
        elif args.command == "backfill": result = run_pipeline(wgs=[args.wg], use_llm=not args.no_llm, meetings=(args.frm, args.to))
        elif args.command == "remap": result = run_remap()
        elif args.command == "enrich":
            overrides = {"max_calls": args.max_calls, "batch_size": args.batch_size}
            result = run_enrich(**overrides) if any(value is not None for value in overrides.values()) else run_enrich()
        elif args.command == "meeting-digests":
            result = run_meeting_digests(max_calls=args.max_calls) if args.max_calls is not None else run_meeting_digests()
        elif args.command == "feature-evolution":
            result = run_pipeline_feature_evolution(max_calls=args.max_calls) if args.max_calls is not None else run_pipeline_feature_evolution()
        elif args.command == "lineage-report": print(build_lineage_report()); return EXIT_OK
        elif args.command == "fetch-docs": return EXIT_OK if run_fetch_docs(wg=args.wg, meeting=args.meeting, agenda=args.agenda) >= 0 else 1
        else: return run_doctor(probe_network=args.network)
    except ParseError as exc:
        logging.error("解析断言失败: %s", exc); return EXIT_PARSE
    for alert in result.alerts: logging.warning("%s", alert)
    return result.exit_code


def _positive_int(value: str, option: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError(f"{option} 必须为正整数")
    return parsed
