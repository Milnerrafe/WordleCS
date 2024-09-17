// This function gets the date and formats it in the standard date format for JavaScript.
const getDate = () => {
  const date = new Date();
  return date.toISOString();
};

// This function gets the most recent database entry and returns the most recent database entry database key. Which is how key value databases work.
const getMostRecentValue = async (Database) => {
  const { keys } = await env.Database.list();

  const sortedKeys = keys.sort((a, b) => {
    const dateA = new Date(a.name.split("-")[1]);
    const dateB = new Date(b.name.split("-")[1]);
    return dateB - dateA;
  });

  const mostRecentKey = sortedKeys[0].name;

  return { key: mostRecentKey };
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // Here we define the variables that we need for our code.
    const var1 = getMostRecentValue();
    const var2 = getDate();
    const var3 =
      "https://raw.githubusercontent.com/getify/dwordly-game/main/five-letter-words.json";

    if (request.method === "GET") {
      // Here we check if today's date matches the date of the most recent database entry. If it doesn't, we create a database entry by using our dictionary of five letter words, randomly sorting them, picking the first 20, then adding them to the database with today's date as the key for the database.
      while (var1 != var2) {
        const response = await fetch(var3);
        const data = await response.json();
        const shuffledData = data.sort(() => Math.random() - 0.5);
        const shortenedArray = shuffledData.slice(0, 20);
        const key = var2;
        await env.Database.put(key, JSON.stringify(shortenedArray));
      }

      // Here, if we have already added a database entry for the day, then we get that JSON and we serve it to the user.
      if (var1 == var2) {
        const response1 = await env.Database.get(var1);
        return new Response(response1);
      } else {
        return new Response(
          "An error has occurred. The most recent value does not equal the date.",
          { status: 500 },
        );
      }
    }

    return new Response("Invalid route or method", { status: 400 });
  },
};
