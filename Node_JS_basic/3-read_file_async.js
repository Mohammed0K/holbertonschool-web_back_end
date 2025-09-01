const fs = require('fs');

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.trim().split('\n').slice(1).filter((line) => line.length > 0);
            console.log(`Number of students: ${lines.length}`);

            const fields = {};
            for (const line of lines) {
                const [firstname, , , field] = line.split(',');
                if (!fields[field]) fields[field] = [];
                fields[field].push(firstname);
            }

            for (const [field, names] of Object.entries(fields)) {
                console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
            }

            resolve();
        });
    });
}

module.exports = countStudents;
