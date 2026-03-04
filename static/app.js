document.addEventListener('DOMContentLoaded', () => {
  const sendBtn = document.getElementById('send');
  const promptEl = document.getElementById('prompt');
  const respEl = document.getElementById('respText');
  const statusEl = document.getElementById('status');
  const modelEl = document.getElementById('model');

  async function send() {
    const prompt = promptEl.value.trim();
    if (!prompt) return;
    sendBtn.disabled = true;
    statusEl.textContent = 'Generando...';
    respEl.textContent = '';

    try {
      const res = await fetch('/api/llm', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, model: modelEl.value }),
      });

      const data = await res.json();
      if (res.ok) {
        respEl.textContent = data.respuesta || JSON.stringify(data, null, 2);
        statusEl.textContent = 'Listo';
      } else {
        respEl.textContent = data.error || JSON.stringify(data, null, 2);
        statusEl.textContent = 'Error';
      }
    } catch (err) {
      respEl.textContent = String(err);
      statusEl.textContent = 'Error';
    } finally {
      sendBtn.disabled = false;
    }
  }

  sendBtn.addEventListener('click', send);

  // submit with Ctrl+Enter inside textarea
  promptEl.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') send();
  });
});
