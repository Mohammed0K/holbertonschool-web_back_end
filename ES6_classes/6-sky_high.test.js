import SkyHighBuilding from './6-sky_high.js';

test('SkyHighBuilding works correctly', () => {
  const b = new SkyHighBuilding(2000, 5);
  expect(b.sqft).toBe(2000);
  expect(b.floors).toBe(5);
  expect(b.evacuationWarningMessage()).toBe('Evacuate slowly the 5 floors');
});
