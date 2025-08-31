import initializeRooms from './1-make_classrooms.js';
import ClassRoom from './0-classroom.js';

test('initializeRooms returns an array of ClassRoom instances', () => {
  const rooms = initializeRooms();
  expect(rooms).toHaveLength(3);
  expect(rooms[0]).toBeInstanceOf(ClassRoom);
  expect(rooms.map(r => r._maxStudentsSize)).toEqual([19, 20, 34]);
});
