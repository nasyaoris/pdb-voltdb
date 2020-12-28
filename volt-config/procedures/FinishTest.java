package onlinetest.procedures;

import org.voltdb.*;

public class FinishTest extends VoltProcedure {
  public final SQLStmt updatePeserta = new SQLStmt(
    "UPDATE PESERTA SET finished=1 WHERE username=?;"
  );

  public VoltTable[] run(String username) throws VoltAbortException {
    voltQueueSQL(updatePeserta, username);
    return voltExecuteSQL();
  }
}
