import Building from './5-building.js';

test('Cannot instantiate Building directly', () => {
  expect(() => new Building(100)).toThrow();
});

class TestBuilding extends Building {
  evacuationWarningMessage() {
    return 'Evacuate now!';
  }
}

test('Subclass must implement evacuationWarningMessage', () => {
  const b = new TestBuilding(200);
  expect(b.sqft).toBe(200);
  expect(b.evacuationWarningMessage()).toBe('Evacuate now!');
});
