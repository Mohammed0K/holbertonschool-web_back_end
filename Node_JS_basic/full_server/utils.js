import fs from 'fs';

export function readDatabase(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.trim().split('\n').slice(1).filter((line) => line.length > 0);
            const fields = {};
            for (const line of lines) {
                const [firstname, , , field] = line.split(',');
                if (!fields[field]) fields[field] = [];
                fields[field].push(firstname);
            }

            resolve(fields);
        });
    });
}
