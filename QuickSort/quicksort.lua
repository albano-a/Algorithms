-- Partition function
local function partition(arr, low, high)
    local pivot = arr[high]
    local i = low - 1

    for j = low, high - 1 do
        if arr[j] <= pivot then
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        end
    end

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
end

-- Quicksort function
local function quicksort(arr, low, high)
    if low < high then
        local pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)
    end
end

-- Example usage
local arr = {5, 9, 3, 1, 6, 8, 2, 4, 7}
quicksort(arr, 1, #arr)

-- Print sorted array
for _, v in ipairs(arr) do
    print(v)
end

