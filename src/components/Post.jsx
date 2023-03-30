import { useState } from 'react';
import './Post.css';

const Post = ({postInfo}) => {
    // information.name, .email, .item, .date, .time
    console.log(`postInfo: ${postInfo[0]}`);
    return (
        <div className="post">
            <div>
                {postInfo.name}, {postInfo.email}
            </div>
            <div>
                {postInfo.item}
            </div>
            <div>
                {postInfo.date}, {postInfo.time}
            </div>
        </div>
    )
}

export default Post;