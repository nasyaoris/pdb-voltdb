import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Home from './pages/Home';
import Clustering from './pages/Clustering';
import Regression from './pages/Regression';

function App() {
  return (
    <div>
      <Router>
      <Navbar/>
      <Switch>
        <Route path='/' exact component={Home}/>
        <Route path='/clustering' exact component={Clustering}/>
        <Route path='/regression' exact component={Regression}/>
      </Switch>
      </Router>
    </div>
  );
}

export default App;
