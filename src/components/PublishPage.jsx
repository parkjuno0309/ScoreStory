import { useState } from 'react';
import Post from './Post';
import PostMaker from './PostMaker';

const PublishPage = ({ posts }) => {
    return (
        <div>
            <PostMaker posts={posts} />
            This is where we will put a form or something to post what you want to lend.
        </div>
    )
}

export default PublishPage;