export default function iterateThroughObject(reportWithIterator) {
  const employees = [];
  for (const i of reportWithIterator) {
    employees.push(i);
  }

  return employees.join(' | ');
}
