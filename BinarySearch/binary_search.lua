function binary_search(A, T)
    local l = 1         -- Start left index at 1
    local r = #A - 1    -- End right index at the length of array

    while l <= r do
        local m = math.floor((l + r) / 2)    -- Calculate middle index

        if A[m] < T then
            l = m + 1
        elseif A[m] > T then
            r = m - 1
        else
            return m -- Return index if the element is found
        end
    end

    return nil
end

local array = {1, 2, 3, 4, 5}
local target = 3

local result = binary_search(array, target)

print(result)
