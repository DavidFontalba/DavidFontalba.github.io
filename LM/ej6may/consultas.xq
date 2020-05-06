(: 1 al 5 :)
for $x in (1 to 5)
return $x

(: categoría: CHILDREN:)
let $x := doc("../ej4may/books.xml")/bookstore/book[@category='CHILDREN']
return $x/title

(:LET:)
let $x := (1 to 5)
return <test>{$x}</test>

(:Libros con índice:)
for $x at $i in doc("../ej4may/books.xml")/bookstore/book/title
order by $x
return <book>{$i}. {data($x)}</book>