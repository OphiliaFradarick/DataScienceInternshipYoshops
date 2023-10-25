import React, { useContext } from 'react';
import { UserContext } from './UserContext';

function Greeting() {
  const user = useContext(UserContext);

  return <h1>Hello, {user.name}!</h1>;
}
