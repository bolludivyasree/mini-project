document.getElementById('generateBtn').addEventListener('click', function () {
    const data = document.getElementById('dataInput').value.trim();
  
    if (!data) {
      alert("Please enter some data to generate the QR code.");
      return;
    }
  
    const qr = new QRious({
      element: document.getElementById('qrcode'),
      value: data,
      size: 200,
      background: 'white',
      foreground: 'black',
    });
  });
  