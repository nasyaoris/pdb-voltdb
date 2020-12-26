package onlinetest.procedures;

import org.voltdb.*;

public class SelectPilihanBySoal extends VoltProcedure {
  public final SQLStmt selectPilihan = new SQLStmt(
    "SELECT * FROM PILIHAN WHERE id_soal=?;"
  );

  public VoltTable[] run(String idSoal) throws VoltAbortException {
    voltQueueSQL(selectPilihan, idSoal);
    return voltExecuteSQL();
  }
}
