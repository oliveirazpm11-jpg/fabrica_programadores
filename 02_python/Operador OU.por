programa {

  funcao inicio() {
     inteiro a,b 
    escreva ("digite o primeiro valor: ")
    leia(a)
    escreva("digite o segundo valor: ")
    leia(b)
    escreva("---comparações---\n")
    escreva("a > b = ",(a>b ou a==b),"\n") //true
    escreva("a >= b = ",(a>=b ou a!=b),"\n") //true
    escreva("a < b = ",(a<b ou a>b),"\n") //false
    escreva("a <= b = ",(a<=b ou a==b),"\n") //false
    escreva("a == b = ",(a==b ou a!=b),"\n") // false
    escreva(" a != b = ",(a!=b ou a<b),"\n") //true
  }
}

