package onlinetest.procedures;

import java.util.Objects;
import org.voltdb.*;

public class GetFinalScore extends VoltProcedure {
  public final SQLStmt selectJawaban = new SQLStmt(
    "SELECT id_soal, id_pilihan FROM JAWABAN WHERE username=?;"
  );
  public final SQLStmt selectSoal = new SQLStmt(
    "SELECT kunci_jawaban FROM SOAL WHERE id_soal=?;"
  );

  public long run(String username) throws VoltAbortException {
    voltQueueSQL(selectJawaban, username);
    VoltTable[] resultsJawaban = voltExecuteSQL();
    VoltTable jawabanTable = resultsJawaban[0];
    long finalScore = 0;

    for (int i = 0; i < jawabanTable.getRowCount(); i++) {
      VoltTableRow jawabanRow = jawabanTable.fetchRow(i);
      String idSoal = jawabanRow.getString(0);
      String idPilihan = jawabanRow.getString(1);

      voltQueueSQL(selectSoal, idSoal);
      VoltTable[] resultsSoal = voltExecuteSQL();
      VoltTable soalTable = resultsSoal[0];
      VoltTableRow soalRow = soalTable.fetchRow(0);

      String kunciSoal = soalRow.getString(0);

      if (Objects.equals(idPilihan, kunciSoal)) {
        finalScore += 4;
      } else {
        finalScore -= 1;
      }
    }

    return finalScore;
  }
}
