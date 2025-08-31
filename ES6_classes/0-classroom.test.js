import ClassRoom from './0-classroom.js';

describe('ClassRoom', () => {
  it('should create a classroom with the correct maxStudentsSize', () => {
    const room = new ClassRoom(10);
    expect(room._maxStudentsSize).toBe(10);
  });
});
