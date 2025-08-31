import { listOfStudents } from './9-hoisting.js';

test('listOfStudents has 5 students with correct descriptions', () => {
  expect(listOfStudents).toHaveLength(5);
  expect(listOfStudents[0].fullStudentDescription).toBe('Guillaume Salva - 2020 - San Francisco');
  expect(listOfStudents[4].fullStudentDescription).toBe('Jason Sandler - 2019 - San Francisco');
});
