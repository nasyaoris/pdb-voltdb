package onlinetest.procedures;

import org.voltdb.*;

public class AddPeserta extends VoltProcedure {
  public final SQLStmt insertPeserta = new SQLStmt(
    "INSERT INTO PESERTA VALUES (?,?,?,0);"
  );

  public VoltTable[] run(String username, String password, String name) throws VoltAbortException {
    voltQueueSQL(insertPeserta, username, password, name);
    return voltExecuteSQL();
  }
}
