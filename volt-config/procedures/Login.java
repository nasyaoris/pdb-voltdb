package onlinetest.procedures;

import org.voltdb.*;

public class Login extends VoltProcedure {
  public final SQLStmt selectPeserta = new SQLStmt(
    "SELECT username, name, finished FROM PESERTA WHERE username=? AND password=?;"
  );

  public VoltTable[] run(String username, String password) throws VoltAbortException {
    voltQueueSQL(selectPeserta, username, password);
    return voltExecuteSQL();
  }
}
