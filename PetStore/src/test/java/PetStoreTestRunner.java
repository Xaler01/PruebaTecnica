import com.intuit.karate.junit5.Karate;

class PetStoreTestRunner {

    @Karate.Test
    Karate testPetStoreApi() {
        return Karate.run("classpath:api/petstore/01_add_pet.feature",
                          "classpath:api/petstore/02_get_pet_Id.feature",
                          "classpath:api/petstore/03_update_pet.feature",
                          "classpath:api/petstore/04_get_pet_by_status.feature").relativeTo(getClass());
    }
}
