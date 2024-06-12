function prime(num)
    if num == 0 then
        return nil
    elseif num % 2 == 0 then
        return "É par"
    else
        return "É ímpar"
    end
end

result = prime(8)

print(result)
