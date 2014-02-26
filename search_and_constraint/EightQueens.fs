// search function

let search (start:'a) (moveFunc:'a -> 'a list) (goalFunc:'a -> bool) =
    let rec recur (current:'a) (previous:'a) (visited: Map<'a,'a>) =
        // visited is a Map linking each state to the prior state
        if Map.containsKey current visited 
        then (false, visited)
        else if goalFunc current
             then (true, Map.add current previous visited)
             else let children = moveFunc current
                  in List.fold (fun acc c -> if fst acc // acc is the tuple (sucess, visited)
                                             then acc
                                             else recur c current (snd acc))
                               (false, Map.add current previous visited)
                               children
    recur start start Map.empty

// 8 Queens details and constrains

type square = Queen | Safe | Unsafe

let board = [for r in [1..8] do for c in [1..8] do yield (r,c), Safe] |> Map.ofList
                     
let targets row col =
    List.filter (fun (r,c) -> (r >= 1) && (r <= 8) && (c >= 1) && (c <= 8))
                [for x in [-8;-7;-6;-5;-4;-3;-2;-1;1;2;3;4;5;6;7;8] do
                 yield! [(row+x, col); (row, col+x); (row+x, col+x); (row-x, col+x)]]
    |> Set.ofList |> Seq.toList
    
let move grid (row:int,col:int) =
    let gridQ = Map.add (row, col) Queen grid
    List.fold (fun g (r,c) -> if Map.find (r,c) g = Safe then Map.add (r,c) Unsafe g else g)
              gridQ
              (targets row col)
    
let available g =
    g |> Map.filter (fun k v -> v = Safe)
      |> Map.toList
      |> List.map (fun (a,b) -> a)

// input functions for search
    
let moveFunc (g:Map<(int*int),square>) =
    let moves = available g
    List.map (fun (r,c) -> move g (r,c)) moves

let goalFunc g =
    let queens = g |> Map.toList |> List.filter (fun (k,v) -> v = Queen)
    List.length queens = 8
    
let s, res = search board moveFunc goalFunc

let result = res |> Map.toList |> List.filter (fun (c,p) -> goalFunc c)  |> (fst << List.head)

let showBoard g =
    [for r in [1..8] do yield [for c in [1..8] do yield Map.find (r,c) g]]

showBoard result