public class ArrayTest {
  public static void main(String[] args) {

    int[] listaDiVoti = {1,3,2,6,6,7,9,8,4,12};
    System.out.println(listaDiVoti[3]);

    for (int i = 0; i < listaDiVoti.length; i++) {
      int element = listaDiVoti[i];
      if (element % 2 != 0) {
        continue;
      }
      if (element == 8) break;
      System.out.println(listaDiVoti[i]);
    }

    String[] listaDiNomi = {"Mario", "Guido", "Marco"};
    System.out.println(listaDiNomi[1]);

    for (String nome: listaDiNomi) {
      System.out.println(nome);
    }
  }
}
