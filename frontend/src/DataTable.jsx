const DataRow = ({ row }) => {
    console.log(row)
  return (
    <tr>
      <td>{row.Age}</td>
      <td>{row.AnnualIncome}</td>
      <td>{row.ApplicationDate.$date}</td>
      <td>{row.BankruptcyHistory}</td>
    </tr>
  );
};

const DataTable = ({ data }) => {
    
  return (
    <table>
      <thead>
        <th>Age</th>
        <th>AnnualIncome</th>
        <th>Data</th>
        <th>BankruptcyHistory</th>
      </thead>
      {data.map((row) => {
        return <DataRow row={row} key={row._id.$oid} />;
      })}
    </table>
  );
};

export default DataTable;
