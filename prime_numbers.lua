function prime(num)
    if num == 0 then
        return nil
    elseif num % 2 == 0 then
        return "E par"
    else
        return "E ímpar"
    end
end

result = prime(8)

print(result)
