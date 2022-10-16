def solution(A):
    # init local and global max
    max_depth = depth = 0
    # order by tops keeping index
    srt_a = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
    # place to store current peaks (left idx, left val, right idx, right val)
    tops = list(srt_a[0] + srt_a[0])
    
    # iter from big vals to small skipping the top and bedrock
    # top is already in tops and bedrock can't be a wall to water
    for idx, val in srt_a[1:]:
        if val == 1:
            break

        # 0 - for the next left peak, 2 for the right one
        tops_idx = 1
        if idx < tops[0] - 1:
            tops_idx = 0
        elif idx > tops[2] + 1:
            tops_idx = 2
        
        if tops_idx != 1:
            
            # diff from the smaller peak and the lowest in range btw peaks
            bottom = min(
                A[idx:tops[tops_idx]:1-tops_idx]
            )

            # if the lowest is not at the same level as peaks
            if bottom < tops[tops_idx+1]:
                # calc depth for current range and memorize the peak
                depth = min([tops[tops_idx+1], val]) - bottom
                tops[tops_idx], tops[tops_idx+1] = (idx, val)
        max_depth = max([max_depth, depth])
    return max_depth
