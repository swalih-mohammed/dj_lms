import * as React from 'react';
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import School from '@mui/icons-material/School';
import WhatsApp from '@mui/icons-material/WhatsApp'; 
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
// import Avatar from '@mui/material/Avatar';
import ImageIcon from '@mui/icons-material/Image';
import WorkIcon from '@mui/icons-material/Work';
import Headphones from '@mui/icons-material/Headphones';
import LiveTv from '@mui/icons-material/LiveTv';
import LocalLibrary from '@mui/icons-material/LocalLibrary';




const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));



export default function RecipeReviewCard({PriceCard}) {
  // console.log(props.PriceCard, "firing from card")
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  const handleContactUs= ()=>{
    const link = "https://wa.me/7207724191/?text=Please%20help%20me%20to%20join%20the%20course"
    window.open(link, "_blank")
  }

  return (
    <Card raised sx={{ maxWidth: 345 }}>
      <CardHeader
        avatar={
          <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">
            {PriceCard?.avatar}
          </Avatar>
        }
        action={
          <IconButton aria-label="settings">
            <School />
          </IconButton>
        }
        title={PriceCard?.name}
        subheader={PriceCard?.price}
      />
      <CardMedia
        component="img"
        height="300"
        image={PriceCard?.img}
        alt="Paella dish"
      />
      <CardContent>
        {/* <Typography variant="body2" color="text.secondary">
         {PriceCard?.feature}
        </Typography> */}
        <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
      <ListItem>
        <ListItemAvatar>
          <Avatar>
            <LiveTv />
          </Avatar>
        </ListItemAvatar>
        <ListItemText primary="Weekly Live Classes" secondary="From Experienced Teachers" />
      </ListItem>
      <ListItem>
        <ListItemAvatar>
          <Avatar>
            <LocalLibrary />
          </Avatar>
        </ListItemAvatar>
        <ListItemText primary="Exercise" secondary="Game like designed exercises" />
      </ListItem>
      <ListItem>
        <ListItemAvatar>
          <Avatar>
            <Headphones />
          </Avatar>
        </ListItemAvatar>
        <ListItemText primary="Listening Oriented" secondary="Lear through listening" />
      </ListItem>
    </List>
      </CardContent>
      <CardActions disableSpacing>
        <IconButton onClick={handleContactUs} aria-label="add to favorites">
          <WhatsApp sx={{color:'#006D5B'}}/>
        </IconButton>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>

      </CardActions>
     
    </Card>
  );
}
