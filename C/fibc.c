long q(){
    long g = 1;
    long k = 0;
    while(1){
        g = (1103515245 * g + 12345) % 67108864;
        k = k + 1;
        if (g == 1){
            break;
        }
    }
    return k;
}