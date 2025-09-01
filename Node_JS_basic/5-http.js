const http = require('http');
const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.trim().split('\n').slice(1).filter((line) => line.length > 0);
            const report = [];
            report.push(`Number of students: ${lines.length}`);

            const fields = {};
            for (const line of lines) {
                const [firstname, , , field] = line.split(',');
                if (!fields[field]) fields[field] = [];
                fields[field].push(firstname);
            }

            for (const [field, names] of Object.entries(fields)) {
                report.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }

            resolve(report.join('\n'));
        });
    });
}

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    if (req.url === '/') {
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
        const path = process.argv[2];
        countStudents(path)
            .then((output) => {
                res.end(`This is the list of our students\n${output}`);
            })
            .catch(() => {
                res.end('This is the list of our students\nCannot load the database');
            });
    } else {
        res.end('Hello Holberton School!');
    }
});

app.listen(1245);

module.exports = app;
