##### Smart Game Format

1. SGF is the abbreviation of 'Smart Game Format'. The file format is designed to store game records of board games for two players. It's a text only, tree based format. Therefore games stored in this format can easily be emailed, posted or processed with text-based tools. The main purposes of SGF are to store records of played games and to provide features for storing annotated and analyzed games (e.g. board markup, variations).
2. Example
	* ( ;GM[1] SZ[19] HA[0] KM[3又3/4子] AP[MultiGo:4.4.4] DT[2018-02-06] PB[柯洁]BR[9P] PW[朴廷桓]WR[9P] GN[柯朴十番棋第1局] PC[北京] RE[B+R] ;B[pd] ;W[dd] )
	* (;B[pd] ;W[dd])

##### Deterministic finite Automaton

1. Is a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine) that accepts or rejects [strings](https://en.wikipedia.org/wiki/String_(computer_science)) of symbols and only produces a unique computation (or run) of the automaton for each input string.
2. Use DFA to denote the checkerboard.
3. ![gobang](https://ws2.sinaimg.cn/large/006tKfTcgy1g0wyzp27abj30ca01w3ye.jpg)

##### Boyer-Moore

1. The Boyer–Moore string-search algorithm is an efficient string-searching algorithm that is the standard benchmark for practical string-search literature. The algorithm preprocesses the string being searched for (the pattern), but not the string being searched in (the text). It is thus well-suited for applications in which the pattern is much shorter than the text or where it persists across multiple searches. The Boyer-Moore algorithm uses information gathered during the preprocess step to skip sections of the text, resulting in a lower constant factor than many other string search algorithms. In general, the algorithm runs faster as the pattern length increases. The key features of the algorithm are to match on the tail of the pattern rather than the head, and to skip along the text in jumps of multiple characters rather than searching every single character in the text.

##### Pseudo Algorithm

1. Before start the algorithm
	* Transform all the pre-known checkerboard into DFA separately denote as *D~p~*
	* Transform the current checkerboard into DFA denote as *D~c~* 
	* Transform all the pre-known checkerboard into String which can be used by Boyer-Moore algorithm  separately denote as *S~p~* ,like *K[1]K[2]K[3]...K[N]* 
	* Transform the current checkerboard into String denote as *S~c~* ,like *C[1]C[2]..C[M]*

2. The pseudo Algorithm

<img src="https://ws1.sinaimg.cn/large/006tKfTcgy1g0x0l56h3ij31di0i8qdr.jpg" style="zoom:50%"/>

#### Bibliographical Review

##### Turn-Based

1. The Gobang game is turn-based, which means that the defender takes a step then the attacker takes a step.

##### Perfect Information Game

1. In [game theory](https://en.wikipedia.org/wiki/Game_theory), a [sequential game](https://en.wikipedia.org/wiki/Sequential_game) has **perfect information** if each player, when making any decision, is perfectly informed of all the events that have previously occurred, including the "initialization event" of the game (e.g. the starting hands of each player in a card game).

##### System Constituent Parts

1. The knowledge representation part includes the representation and implementation of the game, the knowledge base such as the opening game and ending game libraries, as well as the data structure of the entire game system, which is the basis of the game system. Efficient storage and presentation technology is its main research direction, such as the "bitboards" representation technology of chess. Since chess is 8X8, the basic unit of storage and processing is "bit". When processed by bit, the processing efficiency can be multiplied.
2. The move sequences generation function finds legal moves according to the rules of the game, and the travel generation function can also combine the corresponding chess knowledge to further filter out more reasonable moves, and optimize the order of the move sequences to improve Game tree search efficiency. 
3. The evaluating function is used to evaluate the situation and give appropriate value to reflect the pros and cons of the situation. In most cases, the evaluation value uses an integer value. 
4. Game tree search is the backbone of the game system. The solution of the whole tree is based on the minimax theorem. 

<img src="https://ws1.sinaimg.cn/large/006tKfTcgy1g17ngmfbhwj31ca0lsjuf.jpg">

