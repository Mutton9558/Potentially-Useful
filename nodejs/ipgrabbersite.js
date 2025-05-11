// THIS CODE IS ONLY FOR EDUCATIONAL PURPOSES! DO NOT USE IT FOR MALICIOUS REASONS.
const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.use(express.json());

// list to store grabbed ips
let storedIps = []; 
var count = 1;
// middle man redirect, grabs ip before redirecting
app.get("/redirecttorickroll", async (req, res) => {
    const target = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
    try{
        ipAddress = req.ip;
        if (ipAddress === '::1') {
            ipAddress = '127.0.0.1';
        }
        storedIps.push(`{IP Address ${count}: ${ipAddress}}`);
        count++; 
        res.redirect(target)
    } catch(err){
        res.status(500).send(`Status 500: ${err.message}`);
    }
})

// Our main site
app.get("/", (req, res) => {
  // redirects to the middle man url
    const rickastley = `http://localhost:${PORT}/redirecttorickroll`
    res.status(200);
    res.send(`
        <html>
            <head><title>Rick roll site</title></head>
            <body>
                <a href=${rickastley}>Click for rick roll!</a>
            </body>
        </html>
        `)
})

app.get("/fetchips", async (req, res) => {
    res.send(storedIps);
});

// opens port for our site
app.listen(PORT, (error) =>{
    if(!error)
        console.log(`Server running on port ${PORT}`)
    else 
        console.log(error);
    }
);
