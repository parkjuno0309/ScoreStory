import { useState } from 'react';
import './Post.css';


const Post = ({postInfo}) => {
    // information.name, .email, .item, .date, .time
    return (
      // replace with a Card from bootstrap instead
      <div className="card mb-3">
        <div className="card-body">
        <h6 className="card-text"> {postInfo.name} Needs:</h6>
          <h5 className="card-title">{postInfo.item}</h5>
          <p class="card-text">
            On {postInfo.date} From {postInfo.startTime}-{postInfo.endTime}
          </p>
          <p class="card-text">{postInfo.email}</p>
        </div>
        {/* <div className="post">
          <div className="name-email">
            {postInfo.name}, {postInfo.email}
          </div>
          <div className="item">{postInfo.item}</div>
          <div>
            {postInfo.date}, {postInfo.startTime}-{postInfo.endTime}
          </div>
        </div> */}
      </div>
    );
}

export default Post;