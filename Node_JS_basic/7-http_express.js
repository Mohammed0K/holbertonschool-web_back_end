const express = require('express');
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

const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    const path = process.argv[2];
    countStudents(path)
        .then((output) => {
            res.send(`This is the list of our students\n${output}`);
        })
        .catch(() => {
            res.status(500).send('This is the list of our students\nCannot load the database');
        });
});

app.listen(1245);

module.exports = app;
