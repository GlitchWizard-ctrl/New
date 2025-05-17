const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/greet', (req, res) => {
    const name = req.body.name;
    res.json({ message: `Hello, ${name}!` });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
