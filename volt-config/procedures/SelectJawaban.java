package onlinetest.procedures;

import org.voltdb.*;

public class SelectJawaban extends VoltProcedure {
  public final SQLStmt selectJawaban = new SQLStmt(
    "SELECT * FROM JAWABAN WHERE username=? AND id_soal=?;"
  );

  public VoltTable[] run(String username, String idSoal) throws VoltAbortException {
    voltQueueSQL(selectJawaban, username, idSoal);
    return voltExecuteSQL();
  }
}
