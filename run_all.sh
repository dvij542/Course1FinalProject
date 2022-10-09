INCLUDE_CBF=False
K=3
CURR_ITER=0
N_ITERS=4
# python3 train.py -r 4
for (( c=4; c<=$N_ITERS; c++ ))
do
    echo "Running $c th iteration"
    DISPLAY=:8 ../../CarlaUE4.sh /Game/Maps/RaceTrack -windowed -carla-server -benchmark -fps=30 -quality-level=Low -l & pid=$!
    sleep 25
    python3 module_7.py -r $c
    a=$c
    a=$((a-1))
    kill -9 $(ps -ef | grep carla | awk '{print $2}')
    echo $a
    # F1="run$a""_images/*"
    # F2="run$c""_images/"
    # cp $F1 $F2 -r
    # python3 train.py -r $c
    # echo "run$c""_images/*" 
done