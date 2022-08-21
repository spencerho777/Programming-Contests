
public class cputest {
    public static void main(String[] args){
        long a=0;
        for (int i=0; i<800000; i++){
            for(int j=0; j<400000; j++){
                a++;
            }
        }
        System.out.println("done");
    }
}
