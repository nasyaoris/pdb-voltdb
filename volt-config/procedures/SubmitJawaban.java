package onlinetest.procedures;

import org.voltdb.*;

public class SubmitJawaban extends VoltProcedure {
  public final SQLStmt upsertJawaban = new SQLStmt(
    "UPSERT INTO JAWABAN VALUES (?,?,?);"
  );

  public VoltTable[] run(String username, String idSoal, String idPilihan) throws VoltAbortException {
    voltQueueSQL(upsertJawaban, username, idSoal, idPilihan);
    return voltExecuteSQL();
  }
}
