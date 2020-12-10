
def fizz_buzz(n)
    if n % 15 == 0
        "FizzBuzz"
    elsif n % 3 == 0
        "Fizz"
    elsif n % 5 == 0
        "Buzz"
    else
        n
    end
end

n = 1

while n <= 15 do
    puts fizz_buzz(n)
    n += 1
end