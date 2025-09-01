const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf-8').trim();
        const lines = data.split('\n').slice(1).filter((line) => line.length > 0);

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
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
