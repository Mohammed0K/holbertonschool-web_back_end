import Car from './10-car.js';

test('Car can be cloned', () => {
  const car1 = new Car('Toyota', 'V8', 'red');
  const car2 = car1.cloneCar();

  expect(car2).toBeInstanceOf(Car);
  expect(car2).not.toBe(car1);
});
