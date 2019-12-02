--author: Manuel Sánchez

--replace element from a list
replace :: Eq a => [a] -> a -> a -> [a]
replace [] _ _ = []
replace (x:xs) z y = if (x==z) then (y:xs)
                     else (x:(replace xs z y))


-- Give the difference of two sets
diff :: Eq a => [a] -> [a] -> [a]
diff b1 b2 = [x | x <- b1, notElem x b2]

-- Sort a list
qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (x:xs) = qsort [u | u <- xs, u < x] ++ [x] ++ qsort [u | u <- xs, u > x]


--Given b1 and b2, and x gets all y in b2\b1 and returns the sets b1\x U y  (in order)
get_exchanged_sets :: Ord a => [a] -> [a] -> a -> [[a]]
get_exchanged_sets b1 b2 x =  [qsort b | y <-(diff b2 b1), b <- [(replace b1 x y)]] 



--Given the whole and two sets b1 b2 checks if they fullfill the exchange axiom considering x in b1
exchange_axiom_by_element :: Ord a => [[a]] -> [a] -> [a] -> a-> Bool
exchange_axiom_by_element b b1 b2 x = any (flip elem b) (get_exchanged_sets b1 b2 x)


--Check if two sets in the whole verify the exchange axiom
exchange_axiom :: Ord a => [[a]] -> [a] -> [a] -> Bool
exchange_axiom b b1 b2 = and [(exchange_axiom_by_element b b1 b2 x)| x <- (diff b1 b2)]


--Gets all the possible pairs of sets of the whole
pairing :: [a] -> [(a,a)]
pairing [] = []
pairing (b:bs) = (zip (repeat b) bs) ++ pairing bs 


--Given the whole checks if it is a set of bases of a matroid
matroid_or_not :: Ord a => [[a]] -> Bool
matroid_or_not [] = False
matroid_or_not b = matroid_or_not_pairs b (pairing b)

--Given the whole set grouped in pairs, checks if it is the set of basis of a matroid
matroid_or_not_pairs :: Ord a => [[a]] -> [([a],[a])] -> Bool
matroid_or_not_pairs b [] = True
matroid_or_not_pairs b (p:ps) = (exchange_axiom b (fst p) (snd p)) && matroid_or_not_pairs b ps
