package no.bekk

import scala.annotation.tailrec

object Main extends App{

  val MAX = 1000000
  val MIN = 1

  def isPalindrom(num:Int) = num.toString == num.toString.reverse

  def isPalindromInOctal(num:Int) = {
    val oct = Integer.toOctalString(num)
    oct == oct.reverse
  }

  def isPalindromPair(num:Int) = isPalindrom(num) && isPalindromInOctal(num)

  @tailrec
  def loop(acc:Int, count:Int) : Int = {
    if (count > MAX) acc
    else loop(if (isPalindromPair(count)) acc + 1 else acc, count + 1)
  }

  val result = loop(0, MIN)
  System.out.println(result)
}


