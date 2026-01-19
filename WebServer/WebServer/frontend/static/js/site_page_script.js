document.addEventListener("DOMContentLoaded", function () {

    // crea var constante che prende/legge dall'html tramite id l'elemento select
    const paidFilter = document.getElementById("paidFilter");
    const categoryFilter = document.getElementById("categoryFilter")
    
    const updateUrl = () => {
        // prima crea oggetto const di tipo URL che ...
        // ... prende in automatico la url della pagina es. site/ -> site_list_view

        const newUrl = new URL(window.location.href)
        
        //paidValue è il campo value del option ( /true/false)
        const paidValue = paidFilter.value;
        const categoryValue = categoryFilter.value;

        if(paidValue){
            // setta
            newUrl.searchParams.set("paid",paidValue);
        }else{
            // pulisce
            newUrl.searchParams.delete("paid");
        }
        //
        if(categoryValue){
            newUrl.searchParams.set("category",categoryValue);
        }else{
            newUrl.searchParams.delete("category");
        }
        window.location.href = newUrl.toString();
    };

    paidFilter.addEventListener("change",updateUrl);
    categoryFilter.addEventListener("change",updateUrl);
});