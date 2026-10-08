from ngr.ops import doctor

def test_all_checks_have_names(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda name: "C:/codex.exe")
    assert all(check.name for check in doctor.check_all())

def test_missing_cli_and_bad_config_are_reported(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda name: None)
    assert any("Codex" in check.name and not check.ok for check in doctor.check_all())
    monkeypatch.setattr(doctor, "load_sources", lambda: (_ for _ in ()).throw(RuntimeError("坏配置")))
    assert any("sources" in check.name and not check.ok for check in doctor.check_all())

def test_network_probe_is_opt_in(monkeypatch):
    monkeypatch.setattr(doctor, "_which", lambda name: "x")
    calls = []
    monkeypatch.setattr(doctor, "_probe_3gpp", lambda: calls.append(1) or True)
    doctor.check_all(); assert calls == []
    assert any("3GPP" in check.name for check in doctor.check_all(probe_network=True))

def test_run_doctor_exit_code(monkeypatch, capsys):
    monkeypatch.setattr(doctor, "check_all", lambda **kwargs: [doctor.Check("A", True, "ok")])
    assert doctor.run_doctor() == 0 and "A" in capsys.readouterr().out
    monkeypatch.setattr(doctor, "check_all", lambda **kwargs: [doctor.Check("A", False, "bad")])
    assert doctor.run_doctor() == 1
