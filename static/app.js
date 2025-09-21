document.getElementById('uploadBtn').addEventListener('click', async () => {
  const f = document.getElementById('fileInput').files[0];
  if(!f){ alert('Choose a PDF'); return; }
  const fd = new FormData();
  fd.append('file', f);
  const res = await fetch('/upload', { method:'POST', body: fd });
  const data = await res.json();
  if(data.error){ alert(data.error); return; }
  document.getElementById('results').classList.remove('hidden');
  document.getElementById('resumeText').textContent = data.text;
  document.getElementById('skills').innerHTML = data.skills.map(s=>'<span class="tag">'+s+'</span>').join(' ');
  document.getElementById('scoreBox').textContent = 'Resume Score: ' + data.score + '/10';
});

document.getElementById('genSummaryBtn').addEventListener('click', async () => {
  const highlights = document.getElementById('highlights').value;
  const res = await fetch('/generate_summaries', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({highlights}) });
  const data = await res.json();
  const el = document.getElementById('summaryOptions');
  el.innerHTML = data.options.map(o=>'<div class="tag" style="display:block;margin:6px 0;">'+o+'</div>').join('');
});

document.getElementById('compareBtn').addEventListener('click', async () => {
  const job_title = document.getElementById('jobTitle').value;
  const resume_text = document.getElementById('resumeText').textContent;
  const res = await fetch('/job_compare', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({job_title, resume_text}) });
  const data = await res.json();
  const node = document.getElementById('jobCompareResult');
  node.innerHTML = '<strong>Matches:</strong> ' + (data.matches.join(', ') || 'None') + '<br/><strong>Gaps:</strong> ' + (data.gaps.join(', ') || 'None');
});
