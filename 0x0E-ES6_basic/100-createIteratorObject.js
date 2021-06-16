export default function createIteratorObject(report) {
  const employees = [];
  for (const k of Object.keys(report.allEmployees)) {
    employees.push(...report.allEmployees[k]);
  }
  return employees;
}
