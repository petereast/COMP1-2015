#Variable Roles in COMP1 2015 Pre-release

##Fixed Value
A variable initialised without any calculation and not changed thereafter; for example, we may need to remember the number of array elements in use.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
|`BOARDDIMENSION`|Integer|`6,10,12,41,44`|this is a constant|

##Stepper
A variable stepping through a systematic, predictable succession of values; for example, during iterations, a variable is used to keep a count of the number of repetitions.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
|`Count`|Integer|`10,13`| |
|`Count2`|integer|`12`| |
|`RankNo`|Integer|`41,43,45,154,166`| |
|`FileNo`|Integer|`44,45,155,167`| |

##Most recent holder
A variable holding the latest value encountered when processing a succession of unpredictable values or simply th latest value obtained as input; for example, storing the latest of a series of values input by the user to add to a running total.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
|`WhoseTurn`|String|`18,28,213,237,239`| |
|`TypeOfGame`|String|`24`| |
|`CheckRedumMoveIsLegal`|Boolean|`54,58,60,63,65,66`| |
|`CheckSarrumMoveIsLegal`|Boolean|`69,71,72`| |
|`GisgigirMoveIsLegal`|Boolean|`75,80,83,85,88,91,94,96,99,100`|should be renamed to match format of others?|
|`CheckNabuMoveIsLegal`|Boolean|`103,105,106`| |
|`CheckMarzazPaniMoveIsLegal`|Boolean|`109,111,112`| |
|`CheckEtluMoveIsLegal`|Boolean|`115,117,118`| |
|`MoveIsLegal`|Boolean|`121,123,129,131,134,136,139,141,143,145,147,149,150,222,229`| |
|`StartSquare`|Int|`191,193,209,224`| |
|`FinishSquare`|Int|`192,193,210,224`| |
|`PlayAgain`|Boolean|`211,240,242`| |
|`GameOver`|Boolean|`214,232`| |
|`SampleGame`|String|`215,217`| |



##Most wanted holder
A variable holding the most appropriate value encountered so far; for example, when we search through a set of values for the largest value, we store the largest value we have encountered so far.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
|`PieceType`|String|`125`| |
|`PieceColour`|String|`126`| |

##Gatherer
A variable accumulating the effect of individual values; for example, when we calculate the total of a series of values, we keep a running total of all the values added so far.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
| | | | |

##Transformation
A variable that always gets its new value from a fixed calculation of values of other variables; for example, we might store the result of a conversion of a measurement in inches to a measurement in metres.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
|`Board`|2D List|`197,198,200,201,203,204,208`|Not 100% on this one|
|`StartRank`|Integer|`225`|strange calculation here - why bother?|
|`StartFile`|Integer|`226`|strange calculation here - why bother?|
|`FinishRank`|Integer|`227`|strange calculation here - why bother?|
|`FinishFile`|Integer|`228`|strange calculation here - why bother?|

##Follower
A variable that gets its new value from the old value of some other data item; for example, before updating a variable its current value is copied to the follower.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
| | | | |

##Temporary
A variable holding some value for a short time only; for example, it is used as the intermediate storage when swapping values in variables.

|Variable Name|Data Type|Line Number(s)|Notes|
|-------------|---------|--------------|-----|
| | | | |


