import HolbertonCourse from './2-hbtn_course.js';

test('HolbertonCourse sets and gets attributes correctly', () => {
  const course = new HolbertonCourse('ES6', 10, ['Bob', 'Alice']);
  expect(course.name).toBe('ES6');
  expect(course.length).toBe(10);
  expect(course.students).toEqual(['Bob', 'Alice']);
});

test('HolbertonCourse throws with invalid types', () => {
  expect(() => new HolbertonCourse(123, 10, ['Bob'])).toThrow();
  expect(() => new HolbertonCourse('ES6', 'notNumber', ['Bob'])).toThrow();
  expect(() => new HolbertonCourse('ES6', 10, [123])).toThrow();
});
