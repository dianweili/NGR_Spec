import io, zipfile
from unittest.mock import Mock
from ngr.fetch.docs import fetch_docs
from ngr.models import Meeting

M = Meeting('RAN1',127,'','https://x/TSGR1_127/')
def docx(text):
 b=io.BytesIO()
 with zipfile.ZipFile(b,'w') as z:z.writestr('word/document.xml',f'<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>')
 return b.getvalue()
def outer():
 b=io.BytesIO()
 with zipfile.ZipFile(b,'w') as z:z.writestr('x.docx',docx('Proposal text'))
 return b.getvalue()
def test_filters_extracts_and_reuses(tmp_path):
 base=M.url+'Docs/'; http=Mock(); http.get.side_effect=lambda url: b'<a href="https://x/TSGR1_127/Docs/R1-1.zip">R1-1.zip</a><a href="https://x/TSGR1_127/Docs/R1-2.zip">R1-2.zip</a>' if url==base else outer()
 got=fetch_docs(http,M,None,agenda_prefix='10.2',out_dir=tmp_path,tdoc_agenda={'R1-1.zip':'10.2','R1-2.zip':'10.8'})
 assert len(got)==1 and 'Proposal text' in got[0].read_text(encoding='utf-8')
 http.reset_mock(); fetch_docs(http,M,None,agenda_prefix='10.2',out_dir=tmp_path,tdoc_agenda={'R1-1.zip':'10.2'})
 assert http.get.call_count == 1
